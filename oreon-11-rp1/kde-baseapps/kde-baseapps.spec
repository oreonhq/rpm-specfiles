%global source0_hash none
Name:    kde-baseapps
Summary:        KDE Core Applications
Version: 16.12.2
Release:        1%{?dist}
License: GPL-2.0-only AND LicenseRef-Callaway-GFDL
URL:     http://kde.org/
BuildArch: noarch
Obsoletes: kdebase < 6:4.7.97-10
Obsoletes: kdebase4 < %{version}-%{release}
Requires: %{name}-common = %{version}-%{release}
Requires: kdialog >= %{version}
Requires: keditbookmarks >= %{version}
Requires: kfind >= %{version}
%ifarch %{?qt5_qtwebengine_arches}%{?!qt5_qtwebengine_arches:%{ix86} x86_64 %{arm} aarch64 mips mipsel mips64el}
Requires: konqueror >= %{version}
%endif
# oreon:deps

# /oreon:deps
%description
Metapackage for Core KDE applications.

%package common
Summary: Common files for %{name}
Obsoletes: dolphin4 < 16.12
Obsoletes: dolphin4-libs < 16.12
Obsoletes: kde-baseapps-libs < 16.12
Obsoletes: kde-baseapps-devel < 16.12
Obsoletes: kde-plasma-folderview = 6:16.12
Obsoletes: kdepasswd < 16.12
Obsoletes: libkonq < 16.12
%description common
%{summary}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
# blank

%build

%install

%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n kde-baseapps-common -f %{oreon_filedir}/kde-baseapps-common.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 16.12.2-22
- Prepare for Oreon 11 (RP1)
