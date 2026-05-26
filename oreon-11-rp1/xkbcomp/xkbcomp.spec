Name:       xkbcomp
Version:    1.5.0
Release:    2%{?dist}
Summary:    XKB keymap compiler

License:    MIT-open-group AND HPND-DEC
URL:        https://www.x.org

Source0:    https://www.x.org/pub/individual/app/xkbcomp-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 2ac31f26600776db6d9cd79b3fcd272263faebac7eb85fb2f33c7141b8486060
%global source0_file xkbcomp-1.5.0.tar.xz
# oreon url source checksums end

BuildRequires: make gcc
BuildRequires: libxkbfile-devel
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xorg-macros) >= 1.8

Obsoletes:  xorg-x11-xkb-utils < 7.8

%description
X.Org XKB keymap compiler

%package devel
Summary:    XKB keymap compiler development package
Requires:   pkgconfig
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
X.Org XKB keymap compiler development files

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/xkbcomp-1.5.0.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "2ac31f26600776db6d9cd79b3fcd272263faebac7eb85fb2f33c7141b8486060" || { echo "oreon: Source0 SHA256 mismatch for xkbcomp-1.5.0.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup

%build
%configure --disable-silent-rules
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/xkbcomp
%{_mandir}/man1/xkbcomp.1*

%files devel
%{_libdir}/pkgconfig/xkbcomp.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.0-2
- Prepare for Oreon 11 (RP1)
