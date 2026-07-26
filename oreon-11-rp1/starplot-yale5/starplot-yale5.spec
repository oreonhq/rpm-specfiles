%global source0_hash ec51a60047de18c9c350f8021f3545889f20da07c00f119b27b8cc44af573ebc

%define _dataset yale5

Summary:	Stellar data set for use by the StarPlot tool
Name:		starplot-%{_dataset}
Version:	0.95
Release:	31%{?dist}
License:	LicenseRef-Not-Copyrightable
URL:		http://starplot.org/
Source0:	http://starplot.org/data/%{_dataset}-%{version}.tar.gz

Requires:	starplot >= %{version}
Requires(post):	starplot >= %{version}

BuildArch:	noarch

%description
Stellar data set for use by the StarPlot tool from the [Yale] Bright Star
Catalog, 5th Rev. Ed. (preliminary), Hoffleit and Warren, 1991. The data set
was obtained from the archives of the Astronomical Data Center (ADC) at NASA
Goddard Space Flight Center.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{_dataset}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/starplot/%{_dataset}/orig-data

install -p -m644 %{_dataset}.spec \
  $RPM_BUILD_ROOT%{_datadir}/starplot/%{_dataset}
install -p -m644 orig-data/catalog.dat \
  $RPM_BUILD_ROOT%{_datadir}/starplot/%{_dataset}/orig-data
install -p -m644 orig-data/notes.dat \
  $RPM_BUILD_ROOT%{_datadir}/starplot/%{_dataset}/orig-data
install -p -m644 orig-data/ReadMe \
  $RPM_BUILD_ROOT%{_datadir}/starplot/%{_dataset}/orig-data

touch $RPM_BUILD_ROOT%{_datadir}/starplot/%{_dataset}.stars

%post
starpkg --dataset %{_datadir}/starplot/%{_dataset} --dest %{_datadir}/starplot

%files
%doc Changelog
%doc COPYING
%doc README
%ghost %{_datadir}/starplot/%{_dataset}.stars

%dir %{_datadir}/starplot/%{_dataset}
%{_datadir}/starplot/%{_dataset}/%{_dataset}.spec
%{_datadir}/starplot/%{_dataset}/orig-data

%changelog
%autochangelog
