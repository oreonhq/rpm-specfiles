%global source0_hash 03afb96f6c4d027b9948369bb0351d674a9faf6f922fcbb953a9f59943810693

%global snap hg20151214

Name:           qt4-style-fusion
Version:        0
Release:        24.%{snap}%{?dist}
Summary:        Fusion widget style for Qt4

# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            https://code.google.com/p/fusion-qt4/
# hg clone https://code.google.com/p/fusion-qt4/ qt4-style-fusion
# find qt4-style-fusion -name ".hg" -exec rm -rf {} \;
# tar cJf qt4-style-fusion-hg$(date +%%Y%%m%%d).tar.xz qt4-style-fusion
Source0:        %{name}-%{snap}.tar.xz
# Taken from Qt4 sources
Source1:        qstylehelper.cpp

# Fix build scripts
Patch0:         fusion-qt4_build.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  qt4-devel-private

%{?_qt4_version:Requires: qt4%{?_isa} = %{_qt4_version}}

%description
Qt4 backport of the Qt5 fusion widget style.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}
%patch -P0 -p1
cp -a %{SOURCE1} .

%build
%qmake_qt4 .
make %{?_smp_mflags}

%install
make install INSTALL_ROOT=%{buildroot}

%files
%{_qt4_plugindir}/styles/libfusion.so

%changelog
%autochangelog
