%global source0_hash 93e8147f42826816c32034bd1d425cde3b6c50480b092e0d253e48b0bd2ce9a3

%global	gem_name	opengl

%bcond_with bootstrap

# MIT-LICENSE: MIT
# README.rdoc: MIT
# examples/OrangeBook/3Dlabs-License.txt (etc): BSD-3-Clause
# examples/NeHe: KILLED (license unclear)
# examples/RedBook/aapoly.rb: HPND
# examples/misc/OGLBench.rb: GPL-1.0-or-later OR Artistic-1.0-Perl
# examples/misc/plane.rb: HPND
# examples/misc/fbo_test.rb ??? KILLED
# examples/misc/trislam.rb: GPL-1.0-or-later OR Artistic-1.0-Perl

Name:		rubygem-%{gem_name}
Version:	0.10.0
Release:	40%{?dist}

Summary:	An OpenGL wrapper for Ruby
# SPDX confirmed
License:	MIT
URL:		https://github.com/drbrain/opengl
# Source0:	https://rubygems.org/gems/%%{gem_name}-%%{version}.gem
# The above gem file contains files with unclear license,
# we use a regenerated gem as a Source0 with such files
# removed.
# Source0 is generated using Source1.  
Source0:	%{gem_name}-%{version}-clean.gem
Source1:	create-clean-opengl-gem.sh
# http://www.gnu.org/licenses/old-licenses/gpl-1.0.txt
Source2:	GPLv1.rubygem_opengl
# Fix for -Werror=incompatible-pointer-types
Patch0:	opengl-0.10.0-pointer-types.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2303995#c20
# Mesa 24.2.2 swrast with dril does not expose accum buffers anymore
Patch1:	0001-Remove-requirement-for-accum-buffers.patch

# MRI (CRuby) only
BuildRequires:	gcc
BuildRequires:	ruby-devel
BuildRequires:	rubygems-devel
BuildRequires:	libGL-devel
BuildRequires:	libGLU-devel
BuildRequires:	freeglut-devel
# %%check
%if %{without bootstrap}
BuildRequires:	rubygem(minitest) >= 5
BuildRequires:	%{_bindir}/xvfb-run
BuildRequires:	mesa-dri-drivers
BuildRequires:	rubygem(glu)
BuildRequires:	rubygem(glut)
BuildRequires:	rubygem(matrix)
%endif

%description
An OpenGL wrapper for Ruby. ruby-opengl contains bindings for OpenGL and the
GLU and GLUT libraries.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
License:	MIT AND BSD-3-Clause AND HPND AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
BuildArch:	noarch

%description	doc
Documentation for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}-clean
mv ../%{gem_name}-%{version}-clean.gemspec ./%{gem_name}.gemspec

find examples/ -type f -print0 | xargs --null file | \
	grep CRLF | sed -e 's|:.*$||' | \
	while read f
do
	sed -i -e 's|\r||' $f
done

sed -i.minitest \
	-e 's|MiniTest::Unit::TestCase|Minitest::Test|' \
	lib/opengl/test_case.rb

%patch -P0 -p1 -b .types
%if 0%{?fedora} >= 41
%patch -P1 -p1 -b .accum
%endif

%build
gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}/
cp -pa .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

install -cpm 644 %{SOURCE2} \
	%{buildroot}%{gem_instdir}/examples/misc/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a ./%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/

pushd %{buildroot}
rm -f .%{gem_extdir_mri}/{gem_make.out,mkmf.log}
popd

# cleanups
pushd %{buildroot}%{gem_instdir}
rm -rf \
	.autotest .gemtest .gitignore .travis.yml \
	Gemfile \
	Manifest.txt \
	Rakefile* \
	*gemspec \
	docs/build_install.txt \
	ext/ \
	test/

find examples/ utils/ -type f -perm /100 \
	-exec chmod ugo-x {} \;

popd

rm -f %{buildroot}%{gem_extdir_mri}/lib/opengl/test_case.rb

%check
%if %{with bootstrap}
exit 0
%endif

pushd .%{gem_instdir}

EXPECTED_TEST_MSG="184 runs, 17\(38\|44\|45\) assertions, 6 failures, [12] errors, 14 skips"

export RUBYLIB=%{buildroot}%{gem_extdir_mri}/:$(pwd)/lib:$(pwd)
# try twice
STATUS_ON_FAILURE=true
for trial in 1 2 ; do
	xvfb-run \
		-s "-screen 0 640x480x24" \
		ruby \
			-e "Dir.glob('test/test_*.rb').each { |f| require f }" \
			2>&1 | tee TEST.log
	cat TEST.log | grep -q "$EXPECTED_TEST_MSG" && break || $STATUS_ON_FAILURE
%ifarch i686
%else
	STATUS_ON_FAILURE=false
%endif
%ifarch s390x
%if 0%{?fedora} == 40
	# Currently mesa on F41, s390x is fairly broken
	STATUS_ON_FAILURE=true
%endif
%endif
done
popd

%files
%dir	%{gem_instdir}
%license	%{gem_instdir}/MIT-LICENSE
%doc	%{gem_instdir}/History.md
%doc	%{gem_instdir}/README.rdoc

%{gem_libdir}/
%{gem_extdir_mri}/

%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc	%{gem_docdir}
%doc	%{gem_instdir}/examples/
%doc	%{gem_instdir}/utils/

%changelog
%autochangelog
