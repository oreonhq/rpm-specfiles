%global debug_package %{nil}

Name:		libkkc-data
Version:	0.2.7
Release:	31%{?dist}
Epoch:		1
Summary:	Language model data for libkkc

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		https://github.com/ueno/libkkc/
Source0:	https://github.com/ueno/libkkc/releases/download/v0.3.5/%{name}-%{version}.tar.xz
Patch0:		https://github.com/ueno/libkkc/commit/ba1c1bd3eb86d887fc3689c3142732658071b5f7.patch
# oreon url source checksums begin
%global source0_sha256 9e678755a030043da68e37a4049aa296c296869ff1fb9e6c70026b2541595b99
%global source0_file libkkc-data-0.2.7.tar.xz
# oreon url source checksums end

BuildRequires:	gcc
BuildRequires:	python3-devel
BuildRequires:	python3-marisa
BuildRequires: make

%description
The %{name} package contains the language model data that libkkc uses
at run time.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libkkc-data-0.2.7.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "9e678755a030043da68e37a4049aa296c296869ff1fb9e6c70026b2541595b99" || { echo "oreon: Source0 SHA256 mismatch for libkkc-data-0.2.7.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q
%patch -P0 -p4 -b .orig


%build
export PYTHON=%{__python3}
%configure --disable-static
%make_build


%install
%make_install


%files
%doc COPYING
%{_libdir}/libkkc


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:0.2.7-31
- Import
