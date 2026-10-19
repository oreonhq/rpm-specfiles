%global source0_hash 792791ccf513d84c48bac44ae12fa6988e25d27387f95bbf4dd44dcc8486569f
%global	gem_name	rmagick
%define setIMver() \
%{nil}
Name:		rubygem-%{gem_name}
Version:	6.2.0
Release:        1%{?dist}
Summary:        Ruby binding to ImageMagick
License:	MIT
URL:		https://github.com/rmagick/rmagick
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	rubygem-%{gem_name}-%{version}-full.tar.gz
Source2:	rmagick-create-full-tarball.sh
Obsoletes:	ruby-RMagick < 2.13.2
Provides:	ruby-RMagick = %{version}-%{release}
Provides:	ruby-RMagick%{?_isa} = %{version}-%{release}
Provides:	ruby(RMagick) = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  ruby-devel
BuildRequires:  rubygem(observer)
BuildRequires:  rubygem(pkg-config)
BuildRequires:  rubygem(pry)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygems-devel
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

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
%files -f %{oreon_filedir}/main.list
%files -n rubygem-rmagick-doc -f %{oreon_filedir}/rubygem-rmagick-doc.list

%changelog

%autochangelog
