%global source0_hash 2592c8e528249d65cc38aa6339b99d1f4edfe762f2bf5a510d205481f9edc2b7

%define	gem_name		ruby-opengl

Summary:	OpenGL Interface for Ruby
Name:		rubygem-%{gem_name}
Version:	0.61.0
Release:	23%{?dist}
License:	MIT
URL:		http://ruby-opengl.rubyforge.org/
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:	ruby(release)
BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
Requires:	ruby(rubygems)

Requires:	rubygem(opengl)

Provides:	rubygem(%{gem_name}) = %{version}-%{release}
Obsoletes:	ruby-%{gem_name} <= %{version}-%{release}
Provides:	ruby-%{gem_name} = %{version}-%{release}
Provides:	ruby(%{gem_name}) = %{version}-%{release}

# No provides
Obsoletes:	%{name}-doc < 0.60.2

BuildArch:	noarch

%description
ruby-opengl consists of Ruby extension modules that are bindings 
for the OpenGL, GLU, and GLUT libraries. It is intended to be 
a replacement for -- and uses the code from -- Yoshi's ruby-opengl.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -T
# Gem repack
TOPDIR=$(pwd)
mkdir tmpunpackdir
pushd tmpunpackdir

gem unpack %{SOURCE0}
cd %{gem_name}-%{version}
gem specification -l --ruby %{SOURCE0} > %{gem_name}.gemspec

gem build %{gem_name}.gemspec
mv %{gem_name}-%{version}.gem $TOPDIR

popd
rm -rf tmpunpackdir

%build
mkdir -p ./%{gem_dir}
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}

# Actually no files
rm -rf %{buildroot}%{gem_docdir}

%files
%exclude	%{gem_cache}
%{gem_spec}

%changelog
%autochangelog
