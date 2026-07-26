%global source0_hash 792791ccf513d84c48bac44ae12fa6988e25d27387f95bbf4dd44dcc8486569f

%global	gem_name	rmagick

%define setIMver() \
%if 0%{?fedora}%{?rhel} == %1 \
BuildRequires:	(ImageMagick-devel >= %2 with ImageMagick-devel < %3)\
Requires:		(ImageMagick%{?_isa} >= %2 with ImageMagick%{?_isa} < %3)\
%endif \
%{nil}

Name:		rubygem-%{gem_name}
Version:	6.2.0
Release:	1%{?dist}

Summary:	Ruby binding to ImageMagick
# SPDX confirmed
License:	MIT
URL:		https://github.com/rmagick/rmagick
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
# %%{SOURCE2} %%{version}
Source1:	rubygem-%{gem_name}-%{version}-full.tar.gz
Source2:	rmagick-create-full-tarball.sh

BuildRequires:	gcc-c++
BuildRequires:	rubygems-devel 
BuildRequires:	ruby-devel
BuildRequires:	rubygem(pkg-config)
BuildRequires:	rubygem(observer)
BuildRequires:	rubygem(test-unit)
BuildRequires:	rubygem(rspec)
BuildRequires:	rubygem(pry)
# Due to ext/RMagick/rmmain.cpp test_Magick_version(), for now
# we specify the exact version for ImageMagick
#
# With rmagick <= 5.5.0, ImageMagick X.Y.Z should all match,
# with rmagick >= 6.0.0, ImageMagick X.Y should match.
%if 0%{?fedora}
%setIMver 46 1:7.1 1:7.2
%setIMver 45 1:7.1 1:7.2
%setIMver 44 1:7.1 1:7.2
%setIMver 43 1:7.1 1:7.2
%setIMver 42 1:7.1 1:7.2
%endif

Obsoletes:	ruby-RMagick < 2.13.2
Provides:	ruby-RMagick = %{version}-%{release}
Provides:	ruby-RMagick%{?_isa} = %{version}-%{release}
Provides:	ruby(RMagick) = %{version}-%{release}

%description
RMagick is an interface between Ruby and ImageMagick.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

Obsoletes:	ruby-RMagick-doc < 2.13.2
Provides:	ruby-RMagick-doc = %{version}-%{release}

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -T -n %{gem_name}-%{version} -b 1
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

# permission
find . -name \*.rb -or -name \*.gif | xargs chmod ugo-x 

%build
export MAKE="make %{?_smp_mflags}"
# Make sure that .so is to be created newly
rm -rf ./%{gem_extdir_mri}
gem build %{gem_name}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/
cp -a \
	doc \
	examples \
	%{buildroot}%{gem_instdir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} \
	%{buildroot}%{gem_extdir_mri}/

pushd %{buildroot}%{gem_instdir}
rm -rf \
	.editorconfig \
	.devcontainer \
	.github \
	.gitignore .[^.]*.yml \
	wercker.yml \
	.rspec \
	.simplecov \
	.yardopts \
	Doxyfile Gemfile Rakefile \
	before_*.sh \
	doc/.cvsignore \
	*.gemspec \
	test/ \
	spec/ \
	ext/ \
	benchmarks/ \
	.circleci/ \
	.ruby-version \
	%{nil}
popd

%check
export RUBYLIB=$(pwd):$(pwd)/lib:$(pwd)/test:%{buildroot}%{gem_extdir_mri}
export COVERAGE=false

rm -rf tmp
mkdir tmp

rspec spec/

find spec -name \*.skip | while read f
do
	mv $f ${f%.skip}
done

%files
%dir	%{gem_instdir}/
%license	%{gem_instdir}/LICENSE
%doc	%{gem_instdir}/CONTRIBUTING.md
%doc	%{gem_instdir}/CHANGELOG.md
%doc	%{gem_instdir}/README.md

%{gem_libdir}/
%{gem_extdir_mri}/
%{gem_instdir}/sig/
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc	%{gem_docdir}/
%doc	%{gem_instdir}/CODE_OF_CONDUCT.md
%doc	%{gem_instdir}/doc/
%doc	%{gem_instdir}/examples/

%changelog
%autochangelog
