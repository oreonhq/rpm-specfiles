%global source0_hash 8b8fcf9ce076553c10b730dff628ad30f93f2605bcf0660e2a13d9cada0b2de7
%global alpha 0
Name:           flnet
Version:        7.5.0
Release:        1%{?dist}
Summary:        Amateur Radio Net Control Station
License:        GPL-3.0-or-later
URL:            http://www.w1hkj.com/Net-help/index.html
Source0:        http://www.w1hkj.com/files/%{name}/%{name}-%{version}.tar.gz
Source99:       flnet.appdata.xml
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  fltk-devel
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  make
# /oreon:deps
%description
Net provides the Amateur Radio Net Control Station operator with a real time
tool to assist him or her in managing the net activities.  A single screen with
multiple windows is used to allow rapid entry, search, pick and display of all
stations calling in to the net.  All operations on the main screen are
accomplished with keyboard entries only.  No mouse action is required to
perform the net control functions.  Experience has shown that most net control
operators prefer this method of operation to improve the speed of entry and
selection.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export LIBS="-lfltk"
%configure
%make_build
%install
%make_install
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/flnet.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
