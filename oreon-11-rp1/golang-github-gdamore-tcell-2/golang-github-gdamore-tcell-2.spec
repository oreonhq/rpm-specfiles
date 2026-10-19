%global source0_hash da6ed9c0239ff902bcd1c4cdf249534e6cfa0d35f1480e53cfcb9dff04b304db
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%bcond system_foot 0
%global goipath         github.com/gdamore/tcell/v2
Version:                2.13.1
%gometa
%global common_description %{expand:
Tcell is an alternate terminal package, similar in some ways to termbox, but
better in others.}
%global golicenses      LICENSE
%global godocs          CHANGESv2.md AUTHORS TUTORIAL.md README.md
%global gosupfiles      webfiles/*
Name:           golang-github-gdamore-tcell-2
Release:        1%{?dist}
Summary:        Alternate terminal package
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://github.com/gdamore/tcell/archive/v%{version}/tcell-%{version}.tar.gz
%if %{without bootstrap}
%if %{with system_foot}
%endif
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1 -q

%if %{without bootstrap}
ls -R terminfo/?/ > terminfo-files
# Use existing sources for:
# * sun, which is hand-coded, not generated
# * xterm-direct, which is hand-coded, not generated
# * ghostty is not yet packaged
skipped=(
    \! -path '*sun/term.go'
)
skipped+=(
    -a \! -path '*xterm/direct.go'
)
skipped+=(
    -a \! -path '*xterm_ghostty/term.go'
)
%if %{without system_foot}
# also use existing source for foot
skipped+=(
    -a \! -path '*foot/foot.go'
)
%endif
find terminfo/?/ "${skipped[@]}" -a -type f -delete
sed -i 's/go run mkinfo.go/$1/g' terminfo/gen.sh
sed -i 's/^alacritty$/alacritty,alacritty-direct|alacritty/g' terminfo/models.txt
%if %{with system_foot}
echo foot >> terminfo/models.txt
%endif
%endif

%if %{without bootstrap}
%build

%gobuild -o %{gobuilddir}/bin/mkinfo terminfo/mkinfo.go
pushd terminfo
bash -x gen.sh %{gobuilddir}/bin/mkinfo
popd
ls -R terminfo/?/ > generated-terminfo-files
diff -u terminfo-files generated-terminfo-files || true
%endif
%install
%gopkginstall
%oreon_autofiles main
%if %{without bootstrap}
%if %{with check}
%check

%gocheck
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
