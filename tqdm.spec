#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tqdm
Version  : 4.62.3
Release  : 109
URL      : https://files.pythonhosted.org/packages/e3/c1/b3e42d5b659ca598508e2a9ef315d5eef0a970f874ef9d3b38d4578765bd/tqdm-4.62.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/e3/c1/b3e42d5b659ca598508e2a9ef315d5eef0a970f874ef9d3b38d4578765bd/tqdm-4.62.3.tar.gz
Summary  : Fast, Extensible Progress Meter
Group    : Development/Tools
License  : MIT MPL-2.0
Requires: tqdm-bin = %{version}-%{release}
Requires: tqdm-python = %{version}-%{release}
Requires: tqdm-python3 = %{version}-%{release}
Requires: colorama
BuildRequires : buildreq-distutils3
BuildRequires : colorama
BuildRequires : pycodestyle

%description
|Logo|
tqdm
====
|Py-Versions| |Versions| |Conda-Forge-Status| |Docker| |Snapcraft|

%package bin
Summary: bin components for the tqdm package.
Group: Binaries

%description bin
bin components for the tqdm package.


%package python
Summary: python components for the tqdm package.
Group: Default
Requires: tqdm-python3 = %{version}-%{release}

%description python
python components for the tqdm package.


%package python3
Summary: python3 components for the tqdm package.
Group: Default
Requires: python3-core
Provides: pypi(tqdm)

%description python3
python3 components for the tqdm package.


%prep
%setup -q -n tqdm-4.62.3
cd %{_builddir}/tqdm-4.62.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1632186345
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/tqdm

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
