%global source0_hash 93e8147f42826816c32034bd1d425cde3b6c50480b092e0d253e48b0bd2ce9a3
%global	gem_name	opengl
%bcond_with bootstrap
Name:		rubygem-%{gem_name}
Version:	0.10.0
Release:        1%{?dist}
Summary:        An OpenGL wrapper for Ruby
License:	MIT
URL:		https://github.com/drbrain/opengl
Source0:        %{gem_name}-%{version}-clean.gem
Source1:	create-clean-opengl-gem.sh
Source2:	GPLv1.rubygem_opengl
Patch0:	opengl-0.10.0-pointer-types.patch
Patch1:	0001-Remove-requirement-for-accum-buffers.patch
%if %{without bootstrap}
%endif
# oreon:deps
BuildRequires:  freeglut-devel
BuildRequires:  gcc
BuildRequires:  libGL-devel
BuildRequires:  libGLU-devel
BuildRequires:  ruby-devel
BuildRequires:  rubygems-devel
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with bootstrap}
exit 0
%endif
pushd .%{gem_instdir}
EXPECTED_TEST_MSG="184 runs, 17\(38\|44\|45\) assertions, 6 failures, [12] errors, 14 skips"
export RUBYLIB=%{buildroot}%{gem_extdir_mri}/:$(pwd)/lib:$(pwd)
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
%endif
done
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-opengl-doc -f %{oreon_filedir}/rubygem-opengl-doc.list

%changelog

%autochangelog
