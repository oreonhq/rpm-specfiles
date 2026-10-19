%global source0_hash f8b2cda7a1051e359b2442d320111477f85740c61831e92a00d6432230a31c7a
Name:    kuser
Summary:        User Manager for KDE
Version: 16.08.3
Release:        28%{?dist}
License: GPL-2.0-or-later AND LicenseRef-Callaway-GFDL
URL:     https://quickgit.kde.org/?p=%{name}.git
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
Patch100: kuser-16.04.0-fedora_defaults.patch
Conflicts:      kdeadmin < 4.10.80
Obsoletes:      kdeadmin < 4.10.80
# oreon:deps
BuildRequires:  kdelibs4-devel
BuildRequires:  kdepimlibs4-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  make
# /oreon:deps
%description
KUser is a tool for managing users and groups on your system.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} .. \
  -DKU_FIRSTUID=1000 -DKU_FIRSTGID=1000
popd
make %{?_smp_mflags} -C %{_target_platform}
%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_kde4_datadir}/applications/kde4/%{name}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
