%global source0_hash bb02464072f769dd9832fd999526734c90eb4d66fb56d5351540a750c88a77f6

Summary: A utility which provides statistics based on the output of diff
Name: diffstat
Version: 1.69
Release: 1%{?dist}
License: X11
URL: https://invisible-island.net/diffstat
Source0:        https://invisible-island.net/archives/diffstat/%{name}-%{version}.tgz
Source1: COPYING

BuildRequires: gcc
BuildRequires: xz
BuildRequires: make

%description
The diff command compares files line by line.  Diffstat reads the
output of the diff command and displays a histogram of the insertions,
deletions and modifications in each file.  Diffstat is commonly used
to provide a summary of the changes in large, complex patch files.

Install diffstat if you need a program which provides a summary of the
diff command's output.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build
%configure
%make_build

%install
%make_install
cp %{SOURCE1} .

%check
make check

%files
%license COPYING
%doc CHANGES README
%{_bindir}/diffstat
%{_mandir}/*/*

%changelog
%autochangelog
