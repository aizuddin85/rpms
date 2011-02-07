# $Id$
# Upstream: Toby Inkster <tobyink@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define real_name HTTP-Link-Parser

Summary: parse HTTP Link headers
Name: perl-HTTP-Link-Parser
Version: 0.100
Release: 1%{?dist}
License: mit
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTTP-Link-Parser/

Source: http://search.cpan.org/CPAN/authors/id/T/TO/TOBYINK/HTTP-Link-Parser-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(Encode)
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker) 
BuildRequires: perl(RDF::Trine) >= 0.112
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More) >= 0.61
BuildRequires: perl(URI) >= 1.30
BuildRequires: perl(URI::Escape) >= 3.00
BuildRequires: perl >= v5.6.0
Requires: perl(Encode)
Requires: perl(RDF::Trine) >= 0.112
Requires: perl(Scalar::Util)
Requires: perl(URI) >= 1.30
Requires: perl(URI::Escape) >= 3.00
Requires: perl >= v5.6.0

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup


%description


%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --skipdeps
%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/HTTP::Link::Parser.3pm*
%dir %{perl_vendorlib}/
%{perl_vendorlib}/HTTP/Link/Parser.pm
%exclude %{perl_vendorarch}/auto/*/*/*/.packlist

%changelog
* Mon Feb 07 2011 Christoph Maser <cmaser.gmx.de> - 0.100-1
- initial package
