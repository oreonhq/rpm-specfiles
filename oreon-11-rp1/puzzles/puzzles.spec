%global source0_hash 816b77dbc21cd3e72d729b678674e9ac01263297297c00324c4a91b8a1748156

Name: puzzles
Version: 20241230.79be403
Release: 4%{?dist}
Summary: A collection of one-player puzzle games

License: MIT
URL: https://www.chiark.greenend.org.uk/~sgtatham/puzzles/
Source0: https://www.chiark.greenend.org.uk/~sgtatham/puzzles/puzzles-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: gtk3-devel
BuildRequires: ImageMagick
BuildRequires: perl-interpreter

%description
This is a collection of small desktop toys, little games that you can
pop up in a window and play for two or three minutes while you take a
break from whatever else you were doing.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

iconv -f ISO88591 -t UTF8 < LICENCE > LICENSE

%build
# The RPM %%cmake macro doesn't work correctly here:
# https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/22FW4APH22LP3CMQGULOY4FMAMAVJ5JK/
mkdir redhat-linux-build
pushd redhat-linux-build
cmake .. -DCMAKE_INSTALL_PREFIX=%{_prefix} -DNAME_PREFIX=puzzles-
popd
%cmake_build

%install
%cmake_install
desktop-file-validate %{buildroot}%{_datadir}/applications/puzzles-*.desktop

%files
%doc README HACKING puzzles.txt
%license LICENSE
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/apps/*

%changelog
%autochangelog
