%global source0_hash 90a054adc2ca81cf93d378db1bc257043c4d3f87e16df143adc24a46f3563ed4

Name:           sugar-record
Version:        201
Release:        13%{?dist}
Summary:        Recording tool for Sugar

License:        MIT
URL:            http://wiki.laptop.org/go/Record
Source0:        http://download.sugarlabs.org/sources/honey/Record/Record-%{version}.tar.bz2

BuildArch:      noarch
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:	gstreamer1-devel
BuildRequires:	gstreamer1-plugins-base-devel
BuildRequires:  sugar-toolkit-gtk3-devel
BuildRequires:  python3-devel

Requires:       sugar
Requires:       sugar-toolkit-gtk3
Requires:       gstreamer1-plugins-base
Requires:       gstreamer1-plugins-good

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

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}/%{sugaractivitydir}/Record.activity/

%find_lang org.laptop.RecordActivity

%files -f org.laptop.RecordActivity.lang
%license COPYING
%doc NEWS
%{sugaractivitydir}/Record.activity/

%changelog
%autochangelog
