%global source0_hash 04a4c1d1679b3ba6f9ff09d2f28ffb22faef458f38904b9222ef252b7e151258

%global         base_name breeze-grub

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:           grub2-breeze-theme
Version: 6.7.4
Release: 1%{?dist}
Summary:        Breeze theme for GRUB

License:        BSD-2-Clause AND CC-BY-SA-4.0 AND GPL-2.0-or-later WITH Font-exception-2.0 AND GPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only)
URL:            https://invent.kde.org/plasma/%{base_name}.git

Source0:        https://download.kde.org/stable/plasma/%{version}/%{base_name}-%{version}.tar.xz
Source1:        https://download.kde.org/stable/plasma/%{version}/%{base_name}-%{version}.tar.xz.sig

Source10: README.fedora

BuildRequires:  findutils
BuildRequires:  kf6-rpm-macros

# matches grub2 pkg archs
ExcludeArch:    s390 s390x %{arm}
%ifnarch aarch64
Requires:       grub2
%else
Requires:       grub2-efi
%endif

# debuginfo.list ends up empty/blank anyway. disable
%global debug_package   %{nil}
%global _grubthemedir /boot/grub2/themes

# when pkg became arch'd
Obsoletes:      grub2-breeze-theme < 5.6.3-2
Provides:       %{base_name} = %{version}-%{release}

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{base_name}-%{version} -p1

install -m644 -p %{SOURCE10} .

%build
# blank

%install
mkdir -p %{buildroot}%{_grubthemedir}/breeze
find breeze/ -type f -and -not -iname \*.license -print0 \
  | xargs -0 -n100 cp -v -t %{buildroot}%{_grubthemedir}/breeze

%files
%license LICENSES
%doc README.fedora
%{_grubthemedir}/breeze

%changelog
%autochangelog
