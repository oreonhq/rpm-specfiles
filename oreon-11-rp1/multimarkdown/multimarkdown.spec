%global source0_hash aa386f54631dbc4e0beeb6b9cf9eb769db95a3f505a69b663140a80008cf0595
%global projectname MultiMarkdown-6
Name:           multimarkdown
Version:        6.7.0
Release:        1%{?dist}
Summary:        Lightweight markup processor to produce HTML, LaTeX, and more
License:        LicenseRef-Callaway-MIT AND ((LicenseRef-Callaway-MIT AND GPL-2.0-only) AND Zlib AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD)
URL:            https://fletcher.github.io/%{projectname}/
Source0:        https://github.com/fletcher/%{projectname}/archive/%{version}/%{projectname}-%{version}.tar.gz
Patch0:         https://github.com/fletcher/%{projectname}/commit/655c0908155758e7c94858af2fb99dc992709075.patch
Provides:       bundled(multimarkdown) = 4.7.1
Provides:       bundled(CuTest)
Provides:       bundled(argtable3)
Provides:       bundled(miniz)
Provides:       bundled(uthash)
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  perl
# /oreon:deps
%description
MultiMarkdown is a superset of the Markdown lightweight markup syntax with
support for additional output formats and features.

Writing with MultiMarkdown allows you to separate the content and structure of
your document from the formatting. You focus on the actual writing, without
having to worry about making the styles of your chapter headers match, or
ensuring the proper spacing between paragraphs. And with a little forethought, a
single plain text document can easily be converted into multiple output formats
without having to rewrite the entire thing or format it by hand. Even better,
you don’t have to write in “computer-ese” to create well formatted HTML or LaTeX
commands. You just write, MultiMarkdown takes care of the rest.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup      -n %{projectname}-%{version} -S git

%build

%cmake
%cmake_build
%install
%cmake_install
rm -f %{buildroot}%{_bindir}/markdown %{buildroot}%{_bindir}/mmd
mkdir -p %{buildroot}%{_datadir}/doc/multimarkdown
mv %{buildroot}%{_datadir}/doc/MultiMarkdown/* %{buildroot}%{_datadir}/doc/multimarkdown
%oreon_autofiles main

%check

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
