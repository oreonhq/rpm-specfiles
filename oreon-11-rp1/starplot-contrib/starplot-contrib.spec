%global source0_hash none

Summary:	Stellar data set for use by the StarPlot tool
Name:		starplot-contrib
Version:	3
Release:	30%{?dist}
License:	LicenseRef-Fedora-Public-Domain
URL:		http://starplot.org/
Source0:	http://starplot.org/data/stars_with_planets%{version}.stars

Requires:	starplot

BuildArch:	noarch

%description
Stellar data set for use by the StarPlot tool contributed by users.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/starplot

install -p -m644 %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/starplot

%files
%{_datadir}/starplot/stars_with_planets3.stars

%changelog
%autochangelog
