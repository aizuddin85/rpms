# $Id$

# Authority: dag

%define rname gettext

Summary: Internationalization for Perl.
Name: perl-Locale-gettext
Version: 1.01
Release: 0
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/gettext/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://search.cpan.org/CPAN/authors/id/P/PV/PVANDRY/%{rname}-%{version}.tar.gz
Patch0: gettext-1.01-fix-example-in-README.patch.bz2
Patch1: gettext-1.01-includes.patch.bz2
Patch2: gettext-1.01-add-iconv.patch.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503

%description
The gettext module permits access from perl to the gettext() family of
functions for retrieving message strings from databases constructed to
internationalize software. 

It provides gettext(), dgettext(), dcgettext(), textdomain() and
bindtextdomain().

%prep
%setup -n %{rname}-%{version}
%patch0 -p1
%patch1 -p1 -b .includes
%patch2 -p0

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
        PREFIX="%{buildroot}%{_prefix}" \
        INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags} \
	OPTIMIZE="%{optflags}"
#%{__make} test

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/perl5/*/*-linux-thread-multi/
%{__rm} -f %{buildroot}%{_libdir}/perl5/vendor_perl/*/*-linux-thread-multi/auto/*{,/*}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%doc %{_mandir}/man?/*
%{_libdir}/perl5/vendor_perl/*/*

%changelog
* Thu Oct 23 2003 Dag Wieers <dag@wieers.com> - 1.01-0
- Initial package. (using DAR)
