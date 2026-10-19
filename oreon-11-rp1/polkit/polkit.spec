%global source0_hash 9b7bc16f086479dcc626c575976568ba4a85d34297a750d8ab3d2e57f6d8b988
Summary:        An authorization framework
Name: polkit
Version: 127
Release:        1%{?dist}
License: LGPL-2.0-or-later
URL: https://github.com/polkit-org/polkit
Source0:        https://github.com/polkit-org/polkit/archive/refs/tags/%{version}.tar.gz#/polkit-127.tar.gz
Source1: polkit.sysusers
Patch1: 0001-polkit-agent-helper-service-simplify-sandbox-rules.patch
Patch2: 0002-agent-helper-Send-standard-error-to-journal.patch
Patch3: 0004-polkitsubject-Fix-GVariant-ref-leak-for-pidfd-withou.patch
Patch4: 0005-Aisle-www.aisle.com-reported-an-issue-with-unsanitiz.patch
Patch5: 0006-Add-Kazakh-translation.patch
Requires: dbus
Recommends: polkit-pkla-compat
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%{?systemd_requires}
Obsoletes: PolicyKit <= 0.10
Provides: PolicyKit = 0.11
Conflicts: polkit-gnome < 0.97
Obsoletes: polkit-desktop-policy < 0.103
Provides: polkit-desktop-policy = 0.103
Obsoletes: polkit-js-engine < 0.120-5
Provides: polkit-js-engine = %{version}-%{release}
Obsoletes: polkit < 0.113-3
# oreon:deps
BuildRequires:  dbus-devel
BuildRequires:  expat-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  git
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(duktape)
BuildRequires:  systemd
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
polkit is a toolkit for defining and handling authorizations.  It is
used for allowing unprivileged processes to speak to privileged
processes.

%package devel
Summary: Development files for polkit
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %name-docs = %{version}-%{release}
Requires: glib2-devel
Obsoletes: PolicyKit-devel <= 0.10
Provides: PolicyKit-devel = 0.11
%description devel
Development files for polkit.

%package docs
Summary: Development documentation for polkit
Requires: %name-devel = %{version}-%{release}
Obsoletes: PolicyKit-docs <= 0.10
Provides: PolicyKit-docs = 0.11
BuildArch: noarch
%description docs
Development documentation for polkit.

%package libs
Summary: Libraries for polkit
%description libs
Libraries files for polkit.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -D authfw=pam \
       -D examples=false \
       -D gtk_doc=true \
       -D introspection=true \
       -D man=true \
       -D session_tracking=logind \
       -D tests=false
%meson_build
%install
%meson_install
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/polkit.conf
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
%find_lang polkit-1
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post polkit.service
%preun

%systemd_preun polkit.service
%postun

%systemd_postun_with_restart polkit.service
%files -f %{oreon_filedir}/main.list
%files -n polkit-devel -f %{oreon_filedir}/polkit-devel.list
%files -n polkit-docs -f %{oreon_filedir}/polkit-docs.list
%files -n polkit-libs -f %{oreon_filedir}/polkit-libs.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 127-3
- Prepare for Oreon 11 (RP1)
