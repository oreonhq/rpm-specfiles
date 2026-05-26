Summary: A utility which provides statistics based on the output of diff
Name: diffstat
Version: 1.68
Release: 7%{?dist}
License: X11
URL: https://invisible-island.net/diffstat
Source0: https://invisible-island.net/archives/diffstat/%{name}-%{version}.tgz
Source1: COPYING
# oreon url source checksums begin
%global source0_sha256 89f9294a8ac74fcef6f1b9ac408f43ebedf8d208e3efe0b99b4acc16dc6582c7
%global source0_file diffstat-1.68.tgz
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/diffstat-1.68.tgz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "89f9294a8ac74fcef6f1b9ac408f43ebedf8d208e3efe0b99b4acc16dc6582c7" || { echo "oreon: Source0 SHA256 mismatch for diffstat-1.68.tgz" >&2; exit 1; })
# oreon verify url source checksums end
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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.68-7
- Prepare for Oreon 11 (RP1)
