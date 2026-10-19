%global source0_hash 90a054adc2ca81cf93d378db1bc257043c4d3f87e16df143adc24a46f3563ed4
Name:           sugar-record
Version:        201
Release:        13%{?dist}
Summary:        Recording tool for Sugar
License:        MIT
URL:            http://wiki.laptop.org/go/Record
Source0:        http://download.sugarlabs.org/sources/honey/Record/Record-%{version}.tar.bz2
BuildArch:      noarch
Requires:       sugar
Requires:       sugar-toolkit-gtk3
Requires:       gstreamer1-plugins-base
Requires:       gstreamer1-plugins-good
# oreon:deps
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  python3-devel
BuildRequires:  sugar-toolkit-gtk3-devel
# /oreon:deps
%description
Record is the basic rich-media capture activity for the laptop. It 
lets you capture still images, video, and/or audio. It has a simple 
interface and works in both laptop and ebook mode. An interface for 
sharing pictures among multi XOs during a picture-taking session is
a hallmark of the Record activity

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Record-%{version}

sed -i 's/python/python3/' setup.py

%build

python3 ./setup.py build
%install
python3 ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true
%py_byte_compile %{python3} %{buildroot}/%{sugaractivitydir}/Record.activity/
%find_lang org.laptop.RecordActivity
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
