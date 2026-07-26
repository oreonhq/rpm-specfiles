%global source0_hash f8b2cda7a1051e359b2442d320111477f85740c61831e92a00d6432230a31c7a

Name:    kuser
Summary: User Manager for KDE
Version: 16.08.3
Release: 28%{?dist}

# Automatically converted from old format: GPLv2+ and GFDL - review is highly recommended.
License: GPL-2.0-or-later AND LicenseRef-Callaway-GFDL
URL:     https://quickgit.kde.org/?p=%{name}.git

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz

## upstreamable patches
Patch100: kuser-16.04.0-fedora_defaults.patch

BuildRequires: kdelibs4-devel >= 4.14
BuildRequires: kdepimlibs4-devel >= 4.14
BuildRequires: make
BuildRequires: libxcrypt-devel

Conflicts:      kdeadmin < 4.10.80
Obsoletes:      kdeadmin < 4.10.80

%description
KUser is a tool for managing users and groups on your system.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} .. \
  -DKU_FIRSTUID=1000 -DKU_FIRSTGID=1000
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%check
desktop-file-validate %{buildroot}%{_kde4_datadir}/applications/kde4/%{name}.desktop

%files
%doc AUTHORS README
%license COPYING*
%{_kde4_bindir}/%{name}
%{_kde4_appsdir}/%{name}/
%{_kde4_datadir}/applications/kde4/%{name}.desktop
%{_kde4_datadir}/config.kcfg/%{name}.kcfg
%{_kde4_docdir}/HTML/en/%{name}/
%{_kde4_iconsdir}/hicolor/*/*/%{name}.*

%changelog
%autochangelog
