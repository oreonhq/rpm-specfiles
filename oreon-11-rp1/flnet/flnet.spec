%global source0_hash 8b8fcf9ce076553c10b730dff628ad30f93f2605bcf0660e2a13d9cada0b2de7

# For test builds, should be set to 0 for release builds.
%global alpha 0

Name:           flnet
Version:        7.5.0
Release:        12%{?dist}
Summary:        Amateur Radio Net Control Station

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://www.w1hkj.com/Net-help/index.html
%if %{alpha}
Source0:        http://www.w1hkj.com/alpha/%{name}/%{name}-%{version}.tar.gz
%else
Source0:        http://www.w1hkj.com/files/%{name}/%{name}-%{version}.tar.gz
%endif
Source99:       flnet.appdata.xml

BuildRequires:  gcc-c++ make
BuildRequires:  fltk-devel >= 1.3.4
%if %{?fedora}
BuildRequires:  flxmlrpc-devel >= 0.1.0
%endif
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

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

%autosetup

%if 0%{?fedora}
# Remove bundled xmlrpc library
rm -rf src/xmlrpcpp
%endif

%build
# Work around fltk-devel bug in RHEL 7.
# https://bugzilla.redhat.com/show_bug.cgi?id=1510482
export LIBS="-lfltk"
%configure
%make_build

%install
%make_install

%if 0%{?fedora}
# Install appdata file
mkdir -p %{buildroot}%{_datadir}/metainfo
install -pm 0644 %{SOURCE99} %{buildroot}%{_datadir}/metainfo/
%endif

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/flnet.desktop
%if 0%{?fedora}
appstream-util validate-relax --nonet \
    %{buildroot}%{_datadir}/metainfo/*.appdata.xml
%endif

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/flnet
%{_datadir}/applications/flnet.desktop
%{?fedora:%{_datadir}/metainfo/%{name}.appdata.xml}
%{_datadir}/pixmaps/flnet.xpm

%changelog
%autochangelog
