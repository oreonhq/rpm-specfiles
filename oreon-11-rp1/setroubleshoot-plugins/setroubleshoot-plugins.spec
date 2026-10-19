%global source0_hash dc2c77cc5ee9c49ad38b25c63e4f921163d309a1f55ec712324c9c943cd68e44
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
%global _python_bytecompile_extra 0
Summary:        Analysis plugins for use with setroubleshoot
Name: setroubleshoot-plugins
Version: 3.3.15
Release:        1%{?dist}
License: GPL-2.0-or-later
URL: https://gitlab.com/setroubleshoot/plugins
Source0:        https://gitlab.com/-/project/24478430/uploads/1d856bff1c9fb16a8c6fc877d7fe91ca/setroubleshoot-plugins-3.3.15.tar.gz
BuildArch: noarch
Requires: setroubleshoot-server >= 3.3.23
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  perl-XML-Parser
BuildRequires:  python3-devel
# /oreon:deps
%description
This package provides a set of analysis plugins for use with
setroubleshoot. Each plugin has the capacity to analyze SELinux AVC
data and system data to provide user friendly reports describing how
to interpret SELinux AVC denials.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure PYTHON=%{__python3}
make PYTHON=%{__python3}
%install 
rm -rf %{buildroot}
%make_install PYTHON=%{__python3} pkgdocdir=%{_pkgdocdir}
%find_lang %{name}
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/setroubleshoot/plugins
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.3.15-6
- Prepare for Oreon 11 (RP1)
