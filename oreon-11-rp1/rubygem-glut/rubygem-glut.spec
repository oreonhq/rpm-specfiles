%global source0_hash a067b4023f2a64410b48b2da47fdf222310ba82d5b716f4aa4237d32f4f494f7

%global	gem_name	glut

Name:		rubygem-%{gem_name}
Version:	8.3.0
Release:	32%{?dist}

Summary:	Glut bindings for the OpenGL gem
# SPDX confirmed
License:	MIT
URL:		https://github.com/larskanis/glut
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Fix module method function definition argument
# detected by c99 -Werror=incompatible-pointer-types
Patch0:	glut-8.3.0-module-func-argument-c99.patch

BuildRequires:	gcc
BuildRequires:	rubygems-devel 
BuildRequires:	ruby-devel
BuildRequires:	libGL-devel
BuildRequires:	libGLU-devel
BuildRequires:	freeglut-devel

%description
Glut bindings for the opengl gem.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec ./

%patch -P0 -p1

%build
gem build %{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/

pushd %{buildroot}
rm -f .%{gem_extdir_mri}/{gem_make.out,mkmf.log}
popd

rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -rf \
	.autotest .gemtest .gitignore .travis.yml \
	Rakefile \
	ext/ \
	*.gemspec \
	%{nil}
popd

# No test suite available

%files
%dir	%{gem_instdir}
%license	%{gem_instdir}/MIT-LICENSE
%doc	%{gem_instdir}/History.rdoc
%doc	%{gem_instdir}/Manifest.txt
%doc	%{gem_instdir}/README.rdoc

%{gem_libdir}/
%{gem_extdir_mri}/

%{gem_spec}

%files doc
%doc	%{gem_docdir}

%changelog
%autochangelog
