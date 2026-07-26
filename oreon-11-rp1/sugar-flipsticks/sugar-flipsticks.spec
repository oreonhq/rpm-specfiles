%global source0_hash a808a1da9e20b963ede0a935643a103548b56c0f61839004f0ff591f969d3726

Name:           sugar-flipsticks
Version:        14
Release:        12%{?dist}
Summary:        A keyframe animation activity for Sugar
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://wiki.sugarlabs.org/go/Activities/Flip_Sticks

Source0:        http://download.sugarlabs.org/sources/honey/FlipSticks/FlipSticks-%{version}.tar.bz2
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  sugar-toolkit-gtk3 >= 0.116
BuildRequires:  gettext
Requires:       sugar >= 0.116

%description
Flipsticks is a keyframe animation activity that lets you pose and program
a stick figure to walk, run, rotate, twist, tumble and dance. You can save
your animations to the journal and will soon be able to share them via the
mesh. Flipsticks can be used to explore concepts in geometry, computer
programming and animation; it helps develop spatial and analytical thinking
skills. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n FlipSticks-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{__python3} %{buildroot}/%{sugaractivitydir}/FlipSticks.activity/

%find_lang org.worldwideworkshop.olpc.FlipSticks

%files -f org.worldwideworkshop.olpc.FlipSticks.lang
%license COPYING
%doc AUTHORS NEWS TODO
%{sugaractivitydir}/FlipSticks.activity/

%changelog
%autochangelog
