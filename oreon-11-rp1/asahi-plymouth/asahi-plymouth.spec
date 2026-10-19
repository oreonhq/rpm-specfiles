%global source0_hash 9babbffb05f6039f232c328593d6342271894dfce6c205a4d6ea51e30001552d
Name:           asahi-plymouth
Version:        0.2
Release:        1%{?dist}
Summary:        Plymouth theme for Asahi Linux
License:        GPL-3.0-or-later AND CC-BY-SA-4.0
URL:            https://github.com/AsahiLinux/asahi-plymouth
Source0:        https://github.com/AsahiLinux/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
# /oreon:deps
%description

%package -n    plymouth-theme-asahi
Summary:        Plymouth theme for Asahi Linux
Requires:      plymouth
Provides:      %{name} = %{version}-%{release}
%description -n plymouth-theme-asahi

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
mkdir -p %{buildroot}%{_datadir}/plymouth/themes
cp -pr asahi/ %{buildroot}%{_datadir}/plymouth/themes/
%oreon_autofiles plymouth-theme-asahi usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n plymouth-theme-asahi -f %{oreon_filedir}/plymouth-theme-asahi.list

%changelog

%autochangelog
