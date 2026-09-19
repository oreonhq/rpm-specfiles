%global source0_hash 07a8f2b7c09fcdd3d86e0c52adea3c58ca011d0142a93997a01b4af77260ae7b

%if 0%{?rhel} == 7
%global vala_version_api 0.34
%else
%global vala_version_api 0.56
%endif

%global srcurl  http://archive.xfce.org/src/bindings/%{name}

Name:           xfce4-vala
Version:        4.10.3
Release:        44%{?dist}
Summary:        Vala bindings for the Xfce framework

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://wiki.xfce.org/vala-bindings
# caution! %%version may not be evaluable in %%global
Source0:        %{srcurl}/%(echo %{version} |sed s:\..$::)/%{name}-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires: make
BuildRequires: exo-devel
BuildRequires: garcon-devel
BuildRequires: libxfce4ui-devel
BuildRequires: libxfce4util-devel
BuildRequires: xfce4-panel-devel
BuildRequires: xfconf-devel

BuildRequires: vala-devel

# Needed for %%{_datadir}/vala*/vapi directory
Requires: vala(api) = %{vala_version_api}

%description
Xfce4 Vala provides bindings for the Xfce framework

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure --with-vala-api=%{vala_version_api}
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS NEWS README
%{_datadir}/pkgconfig/xfce4-vala.pc
%{_datadir}/vala-%{vala_version_api}/vapi/*

%changelog
%autochangelog
