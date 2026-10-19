%global source1_hash b5e5f90143e535a500353377fba4ada01ab9f361d789ccd639b20e2776281e11
%global source0_hash bd14716ae52d946e37833b3a02d259f5268683af8382c21230c1ce7d767f032a
%global         base_name breeze-grub
ExcludeArch: %{ix86}
Name:           grub2-breeze-theme
Version: 6.7.5
Release:        1%{?dist}
Summary:        Breeze theme for GRUB
License:        BSD-2-Clause AND CC-BY-SA-4.0 AND GPL-2.0-or-later WITH Font-exception-2.0 AND GPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only)
URL:            https://invent.kde.org/plasma/%{base_name}.git
Source0:        https://download.kde.org/stable/plasma/%{version}/%{base_name}-%{version}.tar.xz
Source1:        https://download.kde.org/stable/plasma/%{version}/%{base_name}-%{version}.tar.xz.sig
Source10: README.fedora
ExcludeArch:    s390 s390x %{arm}
%ifnarch aarch64
Requires:       grub2
%else
Requires:       grub2-efi
%endif
%global debug_package   %{nil}
%global _grubthemedir /boot/grub2/themes
Obsoletes:      grub2-breeze-theme < 5.6.3-2
Provides:       %{base_name} = %{version}-%{release}
# oreon:deps
BuildRequires:  findutils
BuildRequires:  kf6-rpm-macros
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{base_name}-%{version} -p1

install -m644 -p %{SOURCE10} .

%build

%install
mkdir -p %{buildroot}%{_grubthemedir}/breeze
find breeze/ -type f -and -not -iname \*.license -print0 \
  | xargs -0 -n100 cp -v -t %{buildroot}%{_grubthemedir}/breeze
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
