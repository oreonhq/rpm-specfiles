%global source0_hash 91c8df4def9631b119d5fcbdd0d98cb708ac2b18ceedaa2f42868f2fd8b2617c
Name:    akonadi-mime
Version: 26.08.0
Release:        1%{?dist}
Summary:        The Akonadi Mime Library
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/pim/%{name}
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
Obsoletes:      kf5-akonadi-mime < 24.01.80-1
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cyrus-sasl-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(shared-mime-info)
# /oreon:deps
%description
%{summary}.

%package   devel
Summary:   Development files for %{name}
Requires:  %{name}%{?_isa} = %{version}-%{release}
Requires: cmake(KPim6Akonadi)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name
%oreon_autofiles akonadi-mime-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles akonadi-mime-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n akonadi-mime-devel -f %{oreon_filedir}/akonadi-mime-devel.list
%files -n akonadi-mime-doc -f %{oreon_filedir}/akonadi-mime-doc.list

%changelog

%autochangelog
