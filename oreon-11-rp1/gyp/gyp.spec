%global source0_hash 1ea6db1064a3cf11565baf35edd39a2e83b954104934b5f67f7717701f075972

%global		revision	fcd686f1
%{expand:	%%global	archivename	gyp-%{version}%{?revision:-git%{revision}}}
%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%if 0%{?rhel} == 5
%global __python2 /usr/bin/python26
%global __os_install_post %__multiple_python_os_install_post
%endif
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

Name:		gyp
Version:	0.1
Release:	0.61%{?revision:.%{revision}git}%{?dist}
Summary:	Generate Your Projects

License:	BSD-3-Clause
URL:		https://gyp.gsrc.io
# No released tarball avaiable. so the tarball was generated
# from svn as following:
#
# 1. git clone https://chromium.googlesource.com/external/gyp
# 2. cd gyp
# 3. version=$(grep version= setup.py|cut -d\' -f2)
# 4. revision=$(git log --oneline|head -1|cut -d' ' -f1)
# 5. tar -a --exclude-vcs -cf /tmp/gyp-$version-git$revision.tar.xz *
Source0:	%{archivename}.tar.xz
Source1:	pyproject.toml
Patch0:		gyp-rpmoptflags.patch
Patch1:		gyp-ninja-build.patch
Patch2:		gyp-python3.patch
Patch3:		gyp-python38.patch
Patch4:		gyp-fix-cmake.patch
Patch5:		gyp-python39.patch
Patch6:		gyp-fips.patch

%if 0%{?rhel}
%if 0%{?rhel} == 5
BuildRequires:	python26-devel
%else
%if 0%{?rhel} < 8
BuildRequires:	python2-devel
%endif
%endif
%if 0%{?rhel} < 8
BuildRequires:	python2-setuptools
Requires:	python2-setuptools
%else
BuildRequires:	python3-devel
Requires:	python3-setuptools
%endif
%else
BuildRequires:	python3-devel
Requires:	python3-setuptools
%endif
BuildRequires:	gcc gcc-c++ ninja-build
BuildArch:	noarch

%description
GYP is a tool to generates native Visual Studio, Xcode and SCons
and/or make build files from a platform-independent input format.

Its syntax is a universal cross-platform build representation
that still allows sufficient per-platform flexibility to accommodate
irreconcilable differences.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -c -n %{archivename}
for i in $(find pylib -name '*.py'); do
	sed -e '\,#![ \t]*/.*python,{d}' $i > $i.new && touch -r $i $i.new && mv $i.new $i
done
cp %{SOURCE1} .
rm setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}

%check
%{__python3} gyptest.py test/hello/gyptest-all.py

%files -f %{pyproject_files}
%license LICENSE
%doc AUTHORS
%{_bindir}/gyp

%changelog
%autochangelog
