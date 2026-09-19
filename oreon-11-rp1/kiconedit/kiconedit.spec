%global source0_hash 2bc42efa3c89bdd14f996ccfedcc11c97e907bb7c97657b93e19e52f464ee50c

Name:    kiconedit
Version: 4.4.0
Release: 36%{?dist}
Summary: An icon editor

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     http://www.kde.org/
Source0: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/extragear/%{name}-%{version}.tar.bz2

BuildRequires: kdelibs4-devel
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: make

%{?_kde4_version:Requires: kdelibs4%{?_isa} >= %{_kde4_version}}

%description
KIconEdit is designed to help create icons for 
KDE using the standard icon palette.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# update docbook version to make doc-translations build with kdelibs >= 4.5
sed -i -e 's#<!DOCTYPE book PUBLIC "-//KDE//DTD DocBook XML V4\.1\.2-Based Variant V1\.1//EN" "dtd/kdex\.dtd" \[#<!DOCTYPE book PUBLIC "-//KDE//DTD DocBook XML V4.2-Based Variant V1.1//EN" "dtd/kdex.dtd" [#g' doc-translations/*_kiconedit/*/index.docbook

%build

mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%find_lang %{name} --with-kde

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/kde4/%{name}.desktop

%files -f %{name}.lang
%doc AUTHORS COPYING COPYING.DOC NEWS
%{_kde4_bindir}/kiconedit
%{_kde4_appsdir}/kiconedit/
%{_kde4_datadir}/applications/kde4/kiconedit.desktop
%{_kde4_iconsdir}/hicolor/*/*/*

%changelog
%autochangelog
