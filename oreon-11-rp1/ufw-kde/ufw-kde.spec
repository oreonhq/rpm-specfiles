%global source0_hash e3fe66f2ba3a226a520070cd7dd6eb94457a045d00769fea2cd0a6d775cc0a69
%global snapdate 20161006
Name:           ufw-kde
Version:        0.5.0
Release:        1%{?dist}
Summary:        UFW control module for KDE
License:        GPL-3.0-only
URL:            https://projects.kde.org/projects/playground/sysadmin/ufw-kde
Source0:        %{name}-%{version}-%{snapdate}.tar.xz
Source1:        ufw-kde.rb
Source2:        ufw-kderc
Source3:        ufw-kde.desktop
Patch0:         ufw-kde-0.5.0-no-env.patch
Patch1:         ufw-kde-0.5.0-rename-strings-h.patch
%global __python %{__python3}
Requires:       ufw
Requires:       python3
Requires:       kde-runtime
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  kdelibs4-devel
BuildRequires:  make
BuildRequires:  python3-devel
# /oreon:deps
%description
KDE KControl Module to configure and control the Uncomplicated Firewall (UFW).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .no-env
%patch -P1 -p1 -b .rename-strings-h

%build

mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ../
popd
make %{?_smp_mflags} -C %{_target_platform}
%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE3}
%py_byte_compile %{__python3} %{buildroot}%{_libexecdir}/kde4/
%find_lang %{name} --all-name --with-kde
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
