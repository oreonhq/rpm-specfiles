%global source0_hash 64d3308ab6016bc95d423d97c6b79a06b2233a82dc43351b0256dc17a2ffc627
Name:           sugar-flipsticks
Version:        14
Release:        1%{?dist}
Summary:        A keyframe animation activity for Sugar
License:        GPL-2.0-or-later
URL:            http://wiki.sugarlabs.org/go/Activities/Flip_Sticks
Source0:        http://download.sugarlabs.org/sources/honey/FlipSticks/FlipSticks-%{version}.tar.bz2
BuildArch:      noarch
Requires:       sugar >= 0.116
# oreon:deps
BuildRequires:  gettext
BuildRequires:  python3-devel
BuildRequires:  sugar-toolkit-gtk3
# /oreon:deps
%description
Flipsticks is a keyframe animation activity that lets you pose and program
a stick figure to walk, run, rotate, twist, tumble and dance. You can save
your animations to the journal and will soon be able to share them via the
mesh. Flipsticks can be used to explore concepts in geometry, computer
programming and animation; it helps develop spatial and analytical thinking
skills. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir FlipSticks-%{version}
%oreon_prep
%build

python3 setup.py build
%install
python3 setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true
%py_byte_compile %{__python3} %{buildroot}/%{sugaractivitydir}/FlipSticks.activity/
%find_lang org.worldwideworkshop.olpc.FlipSticks
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
