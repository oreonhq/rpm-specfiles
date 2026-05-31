%global source0_hash dc2c77cc5ee9c49ad38b25c63e4f921163d309a1f55ec712324c9c943cd68e44

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

# Disable automatic compilation of Python files in extra directories
%global _python_bytecompile_extra 0

Summary: Analysis plugins for use with setroubleshoot
Name: setroubleshoot-plugins
Version: 3.3.15
Release: 6%{?dist}
License: GPL-2.0-or-later
URL: https://gitlab.com/setroubleshoot/plugins
Source0: https://gitlab.com/-/project/24478430/uploads/1d856bff1c9fb16a8c6fc877d7fe91ca/setroubleshoot-plugins-3.3.15.tar.gz
# git format-patch -N setroubleshoot-plugins-<version> -- plugins
# i=1; for j in 00*patch; do printf "Patch%04d: %s\n" $i $j; i=$((i+1));done
BuildArch: noarch

# gcc is needed only for ./configure
# Remove it when the build process is fixed
BuildRequires: gcc
BuildRequires: make
BuildRequires: perl-XML-Parser
BuildRequires: intltool gettext python3-devel
# Introduction of get_package_nvr functions
Requires: setroubleshoot-server >= 3.3.23

%description
This package provides a set of analysis plugins for use with
setroubleshoot. Each plugin has the capacity to analyze SELinux AVC
data and system data to provide user friendly reports describing how
to interpret SELinux AVC denials.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p 1

%build
%configure PYTHON=%{__python3}
make PYTHON=%{__python3}

%install 
rm -rf %{buildroot}
%make_install PYTHON=%{__python3} pkgdocdir=%{_pkgdocdir}
%find_lang %{name}
# Manually invoke the python byte compile macro for each path that needs byte
# compilation.
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/setroubleshoot/plugins

%files -f %{name}.lang 
%doc %{_pkgdocdir}
%{_datadir}/setroubleshoot/plugins

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.3.15-6
- Prepare for Oreon 11 (RP1)
