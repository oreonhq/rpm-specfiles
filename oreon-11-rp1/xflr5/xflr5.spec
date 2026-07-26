%global source0_hash 5bd936f6d0cf14b26a36d1397670943633485ba9c9f65a8ceabcd9b163caa30b

Name:           xflr5
Version:        6.47
Release:        18%{?dist}
Summary:        Analysis tool for airfoils, wings and planes

License:        GPL-3.0-or-later
URL:            http://www.xflr5.com/
Source0:        https://sourceforge.net/projects/xflr5/files/%{version}/%{name}_v%{version}_src.tar.gz
Source1:        %{name}.desktop

# Read library installation directory from env-var
Patch0:         xflr5_libdir.patch

BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  desktop-file-utils
BuildRequires:  texlive-scheme-basic
BuildRequires:  texlive-cm-super
BuildRequires:  tex(inputenc.sty)
BuildRequires:  tex(babel.sty)
BuildRequires:  tex(graphicx.sty)
BuildRequires:  tex(color.sty)
BuildRequires:  tex(hyperref.sty)
BuildRequires:  tex(amsmath.sty)
BuildRequires:  tex(fancyhdr.sty)
BuildRequires:  tex(keystroke.sty)
BuildRequires:  tex(tabularx.sty)
BuildRequires:  tex(multirow.sty)
BuildRequires:  tex(rotating.sty)
BuildRequires:  tex(ecrm1200.tfm)

Requires:       hicolor-icon-theme

%description
XFLR5 is an analysis tool for airfoils, wings and planes operating at low
Reynolds Numbers. It includes:
1. XFoil's Direct and Inverse analysis capabilities
2. Wing design and analysis capabilities based on the Lifiting Line Theory, on
   the Vortex Lattice Method, and on a 3D Panel Method

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}

# Fix FSF addresses
find . -type f -print0 | xargs -0 sed -i 's|59 Temple Place, Suite 330, Boston, MA  02111-1307|51 Franklin Street, Fifth Floor, Boston, MA  02110-1301|'

# Fix line endings
find . -type f -exec dos2unix {} \;

# Build only english documentation
rm -f doc/xflr5-guidelines_latex/guidelines_fr.tex

%build
LIBDIR=%{_lib} %qmake_qt5 PREFIX=%{_prefix} %{name}.pro
# Parallel build broken on s390x...
%ifarch s390x
LIBDIR=%{_lib} make
%else
LIBDIR=%{_lib} %make_build
%endif
make -C doc/xflr5-guidelines_latex
lrelease-qt5 translations/*.ts

# Delete the translations template
rm translations/xflr5v6.qm

%install
make INSTALL_ROOT=%{buildroot} install
install -d %{buildroot}%{_datadir}/%{name}/translations
install -pm 0644 translations/*.qm %{buildroot}%{_datadir}/%{name}/translations
cp -a qss %{buildroot}%{_datadir}/%{name}/qss
install -Dpm 0644 xflr5-gui/images/xflr5_64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
desktop-file-install --dir=%{buildroot}%{_datadir}/applications/ %{SOURCE1}

%files
%doc doc/ReleaseNotes.txt
%doc doc/xflr5-guidelines_latex/guidelines_en.pdf
%license License.txt
%{_bindir}/%{name}
%{_libdir}/libXFoil.so*
%{_libdir}/libxflr5-engine.so*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

%changelog
%autochangelog
