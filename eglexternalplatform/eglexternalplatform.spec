%global debug_package %{nil}

Name:           eglexternalplatform
Version:        1.2.1
Release:        3%{?dist}
Summary:        EGL External Platform Interface headers
License:        MIT
URL:            https://github.com/NVIDIA
BuildArch:      noarch

Source0:        %url/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson

%description
%summary

%package        devel
Summary:        Development files for %{name}

%description    devel
The %{name}-devel package contains the header files for
developing applications that use %{name}.

%prep
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
