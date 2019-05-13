#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x986B408043AE090D (tqdm@caspersci.uk.to)
#
Name     : tqdm
Version  : 4.32.0
Release  : 46
URL      : https://files.pythonhosted.org/packages/e4/7f/fc2d83e8f1cc657e2c06e0f4b7f1e608791843d5e40725561aead5ec4a50/tqdm-4.32.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/e4/7f/fc2d83e8f1cc657e2c06e0f4b7f1e608791843d5e40725561aead5ec4a50/tqdm-4.32.0.tar.gz
Source99 : https://files.pythonhosted.org/packages/e4/7f/fc2d83e8f1cc657e2c06e0f4b7f1e608791843d5e40725561aead5ec4a50/tqdm-4.32.0.tar.gz.asc
Summary  : Fast, Extensible Progress Meter
Group    : Development/Tools
License  : MIT MPL-2.0
Requires: tqdm-bin = %{version}-%{release}
Requires: tqdm-license = %{version}-%{release}
Requires: tqdm-python = %{version}-%{release}
Requires: tqdm-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pycodestyle

%description
|Logo|
tqdm
====
|PyPI-Versions| |PyPI-Status| |Conda-Forge-Status| |Docker| |Snapcraft|

%package bin
Summary: bin components for the tqdm package.
Group: Binaries
Requires: tqdm-license = %{version}-%{release}

%description bin
bin components for the tqdm package.


%package license
Summary: license components for the tqdm package.
Group: Default

%description license
license components for the tqdm package.


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

%description python3
python3 components for the tqdm package.


%prep
%setup -q -n tqdm-4.32.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557779153
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tqdm
cp LICENCE %{buildroot}/usr/share/package-licenses/tqdm/LICENCE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/tqdm

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tqdm/LICENCE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
