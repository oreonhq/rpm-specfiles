%global source0_hash 9a07667d9aef12421d0cdceaa6287f5efbc1e8ad581a4fd07696e0f9dd472d0b
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%global	header_dir	%{ruby_vendorarchdir}
%global	gem_name		cairo
%bcond_with bootstrap
%undefine        _changelog_trimtime
Summary:        Ruby bindings for cairo
Name:		rubygem-%{gem_name}
Version:	1.18.4
Release:        1%{?dist}
License:	GPL-2.0-or-later OR Ruby
URL:		http://cairographics.org/rcairo/
Source0:        http://rubygems.org/downloads/%{gem_name}-%{version}.gem
Source1:	create-cairo-gem.sh
Source11:	rcairo-%{version}-test-missing-files.tar.gz
Source12:	rcairo-create-missing-test-files.sh
Requires:	ruby(release)
%if %{without bootstrap}
%endif
Requires:	rubygems
Provides:	rubygem(%{gem_name}) = %{version}-%{release}
Obsoletes:	ruby-%{gem_name} <= %{version}-%{release}
Provides:	ruby-%{gem_name} = %{version}-%{release}
# oreon:deps
BuildRequires:  cairo-devel
BuildRequires:  dejavu-serif-fonts
BuildRequires:  gcc
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(native-package-installer)
BuildRequires:  rubygem(pkg-config)
BuildRequires:  rubygem(red-colors)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygem(test-unit-notify)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Ruby bindings for cairo. Cairo is a 2D graphics library with support for 
multiple output devices. Currently supported output targets include the 
X Window System, win32, and image buffers.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
%description	doc
This package contains documentation for %{name}.

%package	devel
Summary:	Ruby-cairo development environment
Requires:	%{name} = %{version}-%{release}
Requires:	cairo-devel
Requires:	ruby-devel
%description devel
Header files and libraries for building a extension library for the
ruby-cairo

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

#Patches, etc

# pkg-config dependency should be for development
sed -i  %{gem_name}-%{version}.gemspec \
	-e '\@pkg-config@s|runtime_dependency|development_dependency|' \
	-e '\@native-package-installer@s|runtime_dependency|development_dependency|' \
	%{nil}

%build

gem build %{gem_name}-%{version}.gemspec
%gem_install
rm -rf ./TMPINSTDIR
mkdir -p ./TMPINSTDIR/%{gem_dir}
cp -a ./%{gem_dir}/* ./TMPINSTDIR/%{gem_dir}
TOPDIR=$(pwd)
for f in $(find ./TMPINSTDIR/%{gem_instdir} -name \*.rb)
do
	sed -i -e '/^#!/d' $f
	chmod 0644 $f
done
mkdir -p ./TMPINSTDIR/%{gem_extdir_mri}
cp -a ./%{gem_extdir_mri}/*  TMPINSTDIR/%{gem_extdir_mri}/
pushd ./TMPINSTDIR
mkdir -p .%{header_dir}
mv .%{gem_extdir_mri}/*.h .%{header_dir}/
rm -f .%{gem_extdir_mri}/{gem_make.out,mkmf.log}
popd
%install
cp -a ./TMPINSTDIR/* %{buildroot}/
rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -rf \
	Gemfile \
	Rakefile \
	*.gemspec \
	ext/ \
	test/ \
	%{nil}
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export RUBYLIB=$(pwd)/TMPINSTDIR/%{gem_instdir}:$(pwd)/TMPINSTDIR/%{gem_extdir_mri}/
pushd ./TMPINSTDIR/%{gem_instdir}
rm -rf ./TMPBINDIR
mkdir ./TMPBINDIR
pushd ./TMPBINDIR
ln -sf /bin/true make
export PATH=$(pwd):$PATH
popd
tar xf %{SOURCE11}
cp -a rcairo/test/* test
sed -i -e '\@require .rubygems@a\\ngem "test-unit"\n' test/run-test.rb
sed -i -e "\@require 'bundler/setup'@d" test/run-test.rb
%if %{with bootstrap}
sed -i test/helper.rb -e '\@poppler@s@^@#@'
for f in \
	test/test_context.rb \
	test/test_pdf_surface.rb \
	%{nil}
do
	mv $f $f.orig
done
%endif
ruby ./test/run-test.rb
%files -f %{oreon_filedir}/main.list
%files -n rubygem-cairo-doc -f %{oreon_filedir}/rubygem-cairo-doc.list
%files -n rubygem-cairo-devel -f %{oreon_filedir}/rubygem-cairo-devel.list

%changelog

%autochangelog
