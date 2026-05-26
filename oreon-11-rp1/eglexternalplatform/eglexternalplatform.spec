%global debug_package %{nil}

Name:           eglexternalplatform
Version:        1.2.1
Release:        3%{?dist}
Summary:        EGL External Platform Interface headers
License:        MIT
URL:            https://github.com/NVIDIA
BuildArch:      noarch

Source0:        https://github.com/NVIDIA/eglexternalplatform/archive/1.2.1/eglexternalplatform-1.2.1.tar.gz
# oreon url source checksums begin
%global source0_sha256 5089ceb054ca50c85837f015756a3d0f2f75cf2a98c9e5fbcbcfb8206137f76e
%global source0_file eglexternalplatform-1.2.1.tar.gz
# oreon url source checksums end

BuildRequires:  meson

%description
%summary

%package        devel
Summary:        Development files for %{name}

%description    devel
The %{name}-devel package contains the header files for
developing applications that use %{name}.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/eglexternalplatform-1.2.1.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "5089ceb054ca50c85837f015756a3d0f2f75cf2a98c9e5fbcbcfb8206137f76e" || { echo "oreon: Source0 SHA256 mismatch for eglexternalplatform-1.2.1.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup

%build
%meson

%install
%meson_install

%files devel
%doc README.md samples
%license COPYING
%{_includedir}/*
%{_datadir}/pkgconfig/eglexternalplatform.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.1-3
- Prepare for Oreon 11 (RP1)
