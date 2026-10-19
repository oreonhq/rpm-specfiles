%global source0_hash d41d7dc3eecde6e4339bebdcc731ab9f88a486fe57d7606a48f917c19b0739c6
%global gitver 26b1454a
%global date   20130626
Summary:        Visual tool for Git
Name:          teamgit
Version:       0.0.12
Release:        1%{?dist}
Epoch:         1
License:       GPL-2.0-only
URL:           http://gitorious.org/projects/teamgit
Source0:        %{name}-%{version}-%{date}.tar.xz
Patch01:       teamgit-0.0.12.format.patch
Requires:      git
# oreon:deps
BuildRequires:  avahi-compat-libdns_sd-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  qt-devel
BuildRequires:  source-highlight-qt-devel
# /oreon:deps
%description
This package provides a visual tool for Git, a distributed revision
control system.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
%{qmake_qt4} ./teamgit.pro
make
%install
make INSTALL_ROOT=%{buildroot} install
desktop-file-install --dir %{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/%{name}.desktop
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
