%global source0_hash bf8dd037461016e08c5ad4471b25342df14393583da568fb01c4883a55219ebe

%global shortname implode

Name:           sugar-%{shortname}
Version:        20
Release:        15%{?dist}
Summary:        Implode for Sugar
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://wiki.sugarlabs.org/go/Activities/Implode
Source0:        http://download.sugarlabs.org/sources/honey/Implode/Implode-%{version}.tar.bz2

BuildArch:      noarch
BuildRequires:  gettext
BuildRequires:  python3-devel
BuildRequires:  sugar-toolkit-gtk3
Requires:       sugar

%description
Implode is a logic game based on the "falling block" model of Tetris. The game
starts with a grid partially filled with blocks. The player makes a move by 
removing adjacent blocks of the same color in groups of three or more. When 
blocks are removed, higher blocks fall to fill their space, and when a column 
is cleared, the blocks on either side close to fill the gap. The object of the
game is to remove all the blocks. Since the patterns of blocks above changes
when lower blocks are removed, the player must carefully decide what order
in which to remove the blocks so that there are no isolated blocks left at
the end of the game. The levels are generated in such a way that there is
always a sequence of removals that clears the board. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Implode-%{version}
echo "summary = Logic game based on the “falling block” model of Tetris." >> activity/activity.info

sed -i 's/python/python3/' *.py
sed -i '/^summary/d' activity/activity.info

%build
python3 ./setup.py build

%install
python3 ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true
#executables
find  %{buildroot}%{sugaractivitydir}Implode.activity/*.py -type f | xargs chmod a+x
for file in %{buildroot}%{sugaractivitydir}Implode.activity/{board,boardgen,color,gridwidget,implodeactivity,implodegame,setup}.py; do
   chmod a+x $file
done

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}/%{sugaractivitydir}/Implode.activity/

%find_lang com.jotaro.ImplodeActivity

%files -f com.jotaro.ImplodeActivity.lang
%license COPYING
%{sugaractivitydir}/Implode.activity/

%changelog
%autochangelog
