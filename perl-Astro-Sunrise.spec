#
# Conditional build:
%bcond_without	tests		# perform "make test"
#
%define	pdir	Astro
%define	pnam	Sunrise
Summary:	Astro::Sunrise - Perl extension for computing the sunrise/sunset on a given day
Summary(pl.UTF-8):	Astro::Sunrise - moduł Perla do obliczania wschodów i zachodów Słońca
Name:		perl-Astro-Sunrise
Version:	0.96
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	67c4708fd0d121a5cee8b2bb78297511
URL:		http://search.cpan.org/dist/Astro-Sunrise/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module will return the sunrise and sunset for a given day.

%description -l pl.UTF-8
Ten moduł oblicza momenty wschodów i zachodów Słońca dla
danego dnia.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Astro/Sunrise.pm
%{_mandir}/man3/Astro::Sunrise.*
