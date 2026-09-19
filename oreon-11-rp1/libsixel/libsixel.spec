%global source0_hash b6654928bd423f92e6da39eb1f40f10000ae2cc6247247fc1882dcff6acbdfc8

Name:           libsixel
Version:        1.10.5
Release:        %autorelease
Summary:        SIXEL encoding and decoding

License:        MIT
URL:            https://github.com/libsixel/libsixel
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://github.com/libsixel/libsixel/issues/81
# Taken from https://github.com/libsixel/libsixel/pull/89
Patch:          libsixel-fix-bash-completions.patch

# https://github.com/saitoha/libsixel/issues/200
Patch:          libsixel-fix-cve-2025-9300.patch

# https://github.com/saitoha/libsixel/issues/207
Patch:          libsixel-fix-cve-2025-61146.patch

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(gdlib)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)

%description
An encoder/decoder implementation for DEC SIXEL graphics.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.

%package utils
Summary:        SIXEL encoder and decoder utilities
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description utils
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%meson -Dtests=enabled
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc AUTHORS
%doc NEWS
%doc README.md
%{_libdir}/libsixel.so.1
%{_libdir}/libsixel.so.1.0.0

%files devel
%{_bindir}/libsixel-config
%{_includedir}/sixel.h
%{_libdir}/libsixel.so
%{_libdir}/pkgconfig/libsixel.pc

%files utils
%{_bindir}/img2sixel
%{_bindir}/sixel2png
%{_mandir}/man1/img2sixel.1*
%{_mandir}/man1/sixel2png.1*
%{bash_completions_dir}/img2sixel
%{zsh_completions_dir}/_img2sixel

%changelog
%autochangelog
