%global source0_hash e0b68fb55a41ad28e970ce4c2997f0742af59aa4517ccae371493a78b57fe23d
%bcond check 0
%global goipath         github.com/gdamore/tcell
Version:                3.5.0
%gometa
%global common_description %{expand:
Tcell is a Go package that provides a cell based view for text terminals, like
xterm. It was inspired by termbox, but includes many additional improvements.}
%global golicenses      LICENSE
%global godocs          AUTHORS README.adoc
Name:           %{goname}
Release:        1%{?dist}
Summary:        Alternate terminal package
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/tcell-%{version}.tar.gz
Provides: deprecated()
%global godevelheader   %{shrink:
Provides: deprecated()
}
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
BuildRequires:  kitty-terminfo
BuildRequires:  ncurses
BuildRequires:  ncurses-base
BuildRequires:  ncurses-term
BuildRequires:  rxvt-unicode
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
rm terminfo/?/*/term.go
sed -i 's/go run mkinfo.go/$1/g' terminfo/gen.sh
# Add missing models.
echo alacritty >> terminfo/models.txt
echo xterm-kitty >> terminfo/models.txt

%build

%gobuild -o %{gobuilddir}/bin/mkinfo terminfo/mkinfo.go
pushd terminfo
bash gen.sh %{gobuilddir}/bin/mkinfo
popd
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
