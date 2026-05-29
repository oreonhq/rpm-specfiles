%global source0_hash none
%global source1_hash 249a30268bae5c0982ee4f31abb7126577c03602092a0f2c64b06a4f68176b30
%global source2_hash a288fa98d201a6848ae9642ee62548b2a1f0f5185808d3e668dde6a6e33aaa0a

Name:           double-install
Version:        0
Release:        0%{?dist}
Summary:        Install 2 wheels
License:        BSD-3-Clause AND MIT
%global         markupsafe_version 2.0.1
%global         tldr_version 0.4.4
Source1:        https://github.com/pallets/markupsafe/archive/%{markupsafe_version}/MarkupSafe-%{markupsafe_version}.tar.gz
Source2:        https://files.pythonhosted.org/packages/source/t/tldr/tldr-0.4.4.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel

%description
This package tests that we can build and install 2 wheels at once.
One of them is "noarch" and one has an extension module.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%(test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; })
%(test "%{source2_hash}" = "none" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source2_hash}" || { echo "oreon: Source2 hash mismatch" >&2; exit 1; }; })
%setup -Tc
tar xf %{SOURCE1}
tar xf %{SOURCE2}


%generate_buildrequires
cd markupsafe-%{markupsafe_version}
%pyproject_buildrequires -R
cd ../tldr-%{tldr_version}
%pyproject_buildrequires -R
cd ..


%build
cd markupsafe-%{markupsafe_version}
%pyproject_wheel
cd ../tldr-%{tldr_version}
%pyproject_wheel
cd ..


%install
(
# This should install both the wheels:
%pyproject_install
) 2>&1 | tee install.log
#pyproject_save_files is not possible with 2 dist-infos


%check
# Internal check for the value of %%{pyproject_build_lib}
cd markupsafe-%{markupsafe_version}
%if 0%{?rhel} == 9
test "%{pyproject_build_lib}" == "%{_builddir}/%{buildsubdir}/markupsafe-%{markupsafe_version}/build/lib.%{python3_platform}-%{python3_version}"
%else
test "%{pyproject_build_lib}" == "%{_builddir}/%{buildsubdir}/markupsafe-%{markupsafe_version}/build/lib.%{python3_platform}-cpython-%{python3_version_nodots}"
%endif
cd ../tldr-%{tldr_version}
test "%{pyproject_build_lib}" == "%{_builddir}/%{buildsubdir}/tldr-%{tldr_version}/build/lib"
cd ..
# Internal regression check for %%pyproject_install with multiple wheels
grep 'binary operator expected' install.log && exit 1 || true
grep 'too many arguments' install.log && exit 1 || true


%files
%{_bindir}/tldr*
%pycached %{python3_sitelib}/tldr.py
%{python3_sitelib}/tldr-%{tldr_version}.dist-info/
%{python3_sitearch}/[Mm]arkup[Ss]afe-%{markupsafe_version}.dist-info/
%{python3_sitearch}/markupsafe/
