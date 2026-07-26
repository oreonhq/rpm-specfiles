%global source0_hash 6119cb776a247468df0956bd5d528e27fd6ebb0fb0955439c45cb0a2f317406b

#remove once using %%configure again
%global debug_package %{nil}
%define apricotsdir %{_datadir}/apricots
Name: apricots
Version:  0.2.9
Release:  4%{?dist}
Summary: 2D air combat game

License: GPL-2.0-only
URL: https://github.com/moggers87/apricots
Source0: %{url}/archive/v%{version}/apricots-%{version}.tar.gz       
Source1: apricots.png
#Icon created from screenshot on website
Source2: apricots.desktop

BuildRequires: gcc gcc-c++
BuildRequires: SDL2-devel
BuildRequires: desktop-file-utils
BuildRequires: openal-soft-devel
BuildRequires: alure-devel
BuildRequires: autoconf automake
BuildRequires: make
ExcludeArch: ppc64le aarch64

%description
It's a game where you fly a little plane around the screen and
shoot things and drop bombs on enemy targets, and it's meant to be quick 
and fun.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
./bootstrap
#Use %%configure once --as-needed is fixed, and fix debug at top of spec.
./configure --prefix=%{_prefix}
%make_build

%install
%make_install
mkdir -p %{buildroot}%{_sysconfdir}
install -m 644 apricots/data/apricots.cfg %{buildroot}%{_sysconfdir}
rm %{buildroot}%{_datadir}/apricots/apricots.cfg
ln -s ../../..%{_sysconfdir}/apricots.cfg %{buildroot}%{_datadir}/apricots/apricots.cfg

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install            \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE2}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/apps
install -p -m 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/apps

%files
%license COPYING
%doc AUTHORS ChangeLog README.md
%{_bindir}/apricots
%{_datadir}/apricots
%{_datadir}/applications/apricots.desktop
%{_datadir}/icons/hicolor/24x24/apps/apricots.png
%config(noreplace) %{_sysconfdir}/apricots.cfg

%changelog
%autochangelog
