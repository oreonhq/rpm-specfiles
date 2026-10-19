%global source0_hash 0b4d7cb9cd8c995cbc76856d56b93ff11741559037a20bc38abffb30104b3d4d
%global	gem_name	glu
%bcond_with bootstrap
Name:		rubygem-%{gem_name}
Version:	8.3.0
Release:        37%{?dist}
Summary:        Glu bindings for the opengl gem
License:	MIT
URL:		https://github.com/larskanis/glu
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch1:		rubygem-glu-c99.patch
%if %{without bootstrap}
%endif
# oreon:deps
BuildRequires:  /usr/bin/xvfb-run
BuildRequires:  gcc
BuildRequires:  libGL-devel
BuildRequires:  libGLU-devel
BuildRequires:  mesa-dri-drivers
BuildRequires:  ruby-devel
BuildRequires:  rubygem(glut)
BuildRequires:  rubygem(matrix)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(opengl)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Glu bindings for the opengl gem.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

%build

gem build %{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/
pushd %{buildroot}%{gem_extdir_mri}
rm -f \
	gem_make.out \
	mkmf.log \
	%{nil}
popd
pushd %{buildroot}%{gem_instdir}
rm -rf \
	.autotest .gemtest .gitignore .travis.yml \
	Rakefile \
	ext/ \
	test/
popd
rm -f %{buildroot}%{gem_cache}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{without bootstrap}
pushd .%{gem_instdir}
%ifarch %arm
exit 0
%endif
export RUBYLIB=$(pwd)/lib:$(pwd):%{buildroot}%{gem_extdir_mri}
xvfb-run \
	-s "-screen 0 640x480x24" \
	ruby \
		-e "Dir.glob('test/test_*.rb').each { |f| require f }"
popd
%endif
%files -f %{oreon_filedir}/main.list
%files -n rubygem-glu-doc -f %{oreon_filedir}/rubygem-glu-doc.list

%changelog

%autochangelog
