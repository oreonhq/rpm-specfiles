%global source0_hash c2d19cfc7ce8b150cb50a6b63dc6327c91fb71f76b4f2947e0334a15d5f869d3
%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}
%global realname tktreectrl
Name:		tcl-%{realname}
Version:	2.4.1
Release:        30%{?dist}
Summary:        Multi-column hierarchical listbox widget for Tk
License:	TCL
URL:		http://tktreectrl.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{realname}/%{realname}-%{version}.tar.gz
Obsoletes:	tk-%{realname} < 2.2.3-6
Provides:	%{realname} = %{version}-%{release}
Provides:	tk-%{realname} = %{version}-%{release}
Requires:	tcl(abi) = 8.6 tk
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  tk-devel
# /oreon:deps
%description
TkTreeCtrl is a flexible listbox widget for Tk.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{realname}-%{version}
chmod -x ChangeLog README.txt license.terms doc/*.html generic/*

%build

%configure --with-tcl=%{tcl_sitearch}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
install -d %{buildroot}%{tcl_sitearch}
mv %{buildroot}%{_libdir}/treectrl%{version} %{buildroot}%{tcl_sitearch}/treectrl%{version}
rm -rf $RPM_BUILD_ROOT%{tcl_sitearch}/treectrl%{version}/htmldoc
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
