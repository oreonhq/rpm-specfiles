%global source0_hash b95684bbbaeffbb4a0aa323e2cb0adb6acd445b2e8ad904d82a5488e53721099

%define majorver 8.5
%define vers %{majorver}.7
Summary: Tcl/Tk manual in html format
Name: tcl-html
Version: %{vers}
Release: 29%{?dist}
License: TCL
URL: http://tcl.sourceforge.net/
Source0: http://downloads.sourceforge.net/sourceforge/tcl/tcl%{version}-html.tar.gz
BuildArch: noarch

%description
Tcl/Tk is a powerful scripting language and GUI toolkit.

This package contains the html manual.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n tcl%{version}
cd html 
ln -s contents.htm index.html

##%build
# Nothing to build.

%install
# Nothing to install.

%files
%doc html/*

%changelog
%autochangelog
