%global source0_hash c7954c81d03c43e0ce5faecdbbda678b64d9a4a0f9f897a09cc1a109af388eaa

%define _dataset gliese3

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
Stellar data set for use by the StarPlot tool from the Third Catalogue of
Nearby Stars (preliminary edition), Gliese and Jahreiss, 1991. The data set
was obtained from the archives of the Astronomical Data Center (ADC) at NASA
Goddard Space Flight Center.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{_dataset}-%{version}

# Suppress rpmlint error.
iconv --from-code ISO8859-1 --to-code UTF-8 ./Changelog \
  --output Changelog.utf-8 && mv Changelog.utf-8 ./Changelog
iconv --from-code ISO8859-1 --to-code UTF-8 ./%{_dataset}.spec \
  --output %{_dataset}.utf-8 && mv %{_dataset}.utf-8 ./%{_dataset}.spec

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/starplot/%{_dataset}/orig-data

install -p -m644 %{_dataset}.spec \
  $RPM_BUILD_ROOT%{_datadir}/starplot/%{_dataset}
install -p -m644 orig-data/catalog.dat \
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
